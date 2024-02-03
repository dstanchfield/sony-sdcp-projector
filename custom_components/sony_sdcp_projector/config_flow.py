"""Config flow for Sony SDCP Projector."""

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_HOST
from homeassistant.data_entry_flow import FlowResult
from homeassistant.util.network import is_host_valid

from .const import ATTR_MODEL, DOMAIN


class SonySDCPConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Sony SDCP Projector integration."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize config flow."""
        self.config: dict[str, Any] = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the host step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            if is_host_valid(host):
                self.config[CONF_HOST] = host

                await self.async_set_unique_id(host)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"{ATTR_MODEL}  ({host})", data=user_input
                )

            errors[CONF_HOST] = "invalid_host"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required(CONF_HOST): str}),
            errors=errors,
        )
