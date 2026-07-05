"""Test configuration for Accounts Payable Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "accounts-payable-agent", "category": "Finance"}
