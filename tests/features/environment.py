import logging
import os
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def setup_logging(context):
    """
    Configure logging for test execution
    """
    # Create logs directory
    context.logs_dir = "logs"
    os.makedirs(context.logs_dir, exist_ok=True)

    # Create log file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(context.logs_dir, f"test_execution_{timestamp}.log")

    # Root logger
    context.logger = logging.getLogger()
    context.logger.setLevel(logging.INFO)

    # Remove handlers if behave already set them
    if context.logger.hasHandlers():
        context.logger.handlers.clear()

    # File handler
    context.file_handler = logging.FileHandler(log_file)
    context.file_handler.setLevel(logging.INFO)
    context.file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    # Console handler
    context.console_handler = logging.StreamHandler()
    context.console_handler.setLevel(logging.INFO)
    context.console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )

    context.logger.addHandler(context.file_handler)
    context.logger.addHandler(context.console_handler)

    context.logger.info("=" * 80)
    context.logger.info("Test Execution Started")
    context.logger.info("=" * 80)

def before_all(context):
    # context.config.setup_logging()
    context.screenshot_dir = "screenshots"
    os.makedirs(context.screenshot_dir, exist_ok=True)

    # Create allure results directory
    context.allure_dir = "allure-results"
    os.makedirs(context.allure_dir, exist_ok=True)

    setup_logging(context)

    context.logger.info(f"Screenshots directory: {context.screenshot_dir}")
    context.logger.info(f"Allure results directory: {context.allure_dir}")

def before_feature(context, feature):
    """
    Runs before each feature
    """
    # logger
    context.logger.info("\n" + "="*80)
    context.logger.info(f"Feature: {feature.name}")
    context.logger.info(f"Location: {feature.location}")
    context.logger.info("="*80)

    # Attach feature info to Allure
    allure.dynamic.feature(feature.name)
    if feature.description:
        context.logger.info(f"Description: {' '.join(feature.description)}")

def before_scenario(context, scenario):
    """
    Runs before each scenario - Initialize WebDriver
    """
    print(f"\nScenario: {scenario.name}")


    #logger
    context.logger.info("\n" + "-" * 80)
    context.logger.info(f"Scenario {scenario.name}")
    context.logger.info(f"Tags: {scenario.tags if scenario.tags else 'None'}")
    context.logger.info("-" * 80)

    # Attach scenario info to Allure
    allure.dynamic.title(scenario.name)
    allure.dynamic.description(f"Scenario: {scenario.name}")

    # Add tags to Allure
    for tag in scenario.tags:
        allure.dynamic.tag(tag)

    context.logger.info("Initializing WebDriver...")
    context.logger.info("WebDriver initialized successfully")
    context.driver: WebDriver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demo.openemr.io/b/openemr")

def before_step(context, step):
    """
    Runs before each step
    """
    context.logger.info(f"\n  → Step: {step.keyword} {step.name}")
    context.step_start_time = datetime.now()


def after_step(context, step):
    """
    Runs after each step - Log step status and capture on failure
    """
    step_duration = (datetime.now() - context.step_start_time).total_seconds()

    if step.status == "passed":
        context.logger.info(f"  ✓ Step passed ({step_duration:.2f}s): {step.name}")
    elif step.status == "failed":
        context.logger.error(f"  ✗ Step failed ({step_duration:.2f}s): {step.name}")
        context.logger.error(f"  Error: {step.exception}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"step_failure_{step.name.replace('"', '').replace(' ', '_')}_{timestamp}.png"
        screenshot_path = os.path.join(context.screenshot_dir, screenshot_name)

        context.driver.save_screenshot(screenshot_path)
        context.logger.info(f"  📸 Step failure screenshot: {screenshot_path}")

        # Attach to Allure
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"step_failure_{step.name}",
            attachment_type=AttachmentType.PNG
        )

def after_scenario(context, scenario):
    """
       Runs after each scenario - Capture screenshot on failure
       """
    context.logger.info(f"Scenario status: {scenario.status}")

    if scenario.status == "failed":
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{scenario.name.replace(' ', '_@@@')}_{timestamp}.png"
        screenshot_path = os.path.join(context.screenshot_dir, screenshot_name)
        # Capture screenshot
        context.driver.save_screenshot(screenshot_path)
        context.logger.info(f"📸 Failure screenshot saved: {screenshot_path}")

        # Attach screenshot to Allure
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=f"failure_screenshot",
            attachment_type=AttachmentType.PNG
        )

        # Attach page source
        allure.attach(
            context.driver.page_source,
            name="page_source",
            attachment_type=AttachmentType.HTML
        )

        # Get current URL
        current_url = context.driver.current_url
        context.logger.info(f"Current URL: {current_url}")
        allure.attach(
            current_url,
            name="current_url",
            attachment_type=AttachmentType.TEXT
        )
    elif scenario.status == "skipped":
        context.logger.warning("⊘ Scenario SKIPPED")

    context.driver.quit()


def after_feature(context, feature):
    """
    Runs after each feature
    """
    context.logger.info("\n" + "="*80)
    context.logger.info(f"Feature '{feature.name}' completed")
    context.logger.info(f"Status: {str(feature.status).upper()}")
    context.logger.info("="*80 + "\n")

def after_all(context):
    """
    Runs once after all features - Generate summary
    """

    context.logger.info(f"\n📁 Artifacts Location:")
    context.logger.info(f"  • Screenshots: {os.path.abspath(context.screenshot_dir)}/")
    context.logger.info(f"  • Allure Results: {os.path.abspath(context.allure_dir)}/")

    context.logger.info("\n" + "=" * 80)
    context.logger.info("Test Execution Completed")