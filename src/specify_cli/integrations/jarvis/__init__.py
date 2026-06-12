"""OpenJarvis integration — workspace skills for the ``jarvis`` CLI.

OpenJarvis discovers workspace-local skills from ``./skills/`` and can
execute a one-shot prompt with ``jarvis ask <prompt>``. This integration
installs Spec Kit commands as agentskills.io-compatible
``skills/speckit-<name>/SKILL.md`` files and uses ``AGENTS.md`` for the
managed plan-context section.
"""

from __future__ import annotations

from ..base import IntegrationOption, SkillsIntegration


class JarvisIntegration(SkillsIntegration):
    """Integration for OpenJarvis."""

    key = "jarvis"
    config = {
        "name": "OpenJarvis",
        "folder": "./",
        "commands_subdir": "skills",
        "install_url": "https://open-jarvis.github.io/OpenJarvis/getting-started/install/",
        "requires_cli": True,
    }
    registrar_config = {
        "dir": "./skills",
        "format": "markdown",
        "args": "$ARGUMENTS",
        "extension": "/SKILL.md",
    }
    context_file = "AGENTS.md"

    @classmethod
    def options(cls) -> list[IntegrationOption]:
        return [
            IntegrationOption(
                "--skills",
                is_flag=True,
                default=True,
                help="Install as agent skills (default for OpenJarvis)",
            ),
        ]

    def build_exec_args(
        self,
        prompt: str,
        *,
        model: str | None = None,
        output_json: bool = True,
    ) -> list[str] | None:
        """Build non-interactive CLI args for OpenJarvis.

        OpenJarvis exposes one-shot prompting through ``jarvis ask``.
        The public docs do not advertise model-selection or JSON-output
        flags, so this integration ignores those optional hints and
        captures plain stdout when non-streaming dispatch is requested.
        """
        del model, output_json
        return [self.key, "ask", prompt]
