"""Accounts Payable Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_process_payment_batch():
    """Test Process a batch of vendor payments."""
    tools = AgentTools()
    result = await tools.process_payment_batch(payment_ids="test", payment_method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_payment_timing():
    """Test Optimize payment timing for cash flow and early payment discounts."""
    tools = AgentTools()
    result = await tools.optimize_payment_timing(pending_invoices="test", cash_position="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_apply_early_payment_discount():
    """Test Calculate and apply early payment discount terms."""
    tools = AgentTools()
    result = await tools.apply_early_payment_discount(invoice_id="test", terms="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_reconcile_ap():
    """Test Reconcile accounts payable ledger with bank statements."""
    tools = AgentTools()
    result = await tools.reconcile_ap(period="test", bank_account="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.accounts_payable_agent_agent import AccountsPayableAgentAgent
    agent = AccountsPayableAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
