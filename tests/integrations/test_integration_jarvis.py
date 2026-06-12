"""Tests for JarvisIntegration."""

from specify_cli.integrations import get_integration

from .test_integration_base_skills import SkillsIntegrationTests


class TestJarvisIntegration(SkillsIntegrationTests):
    KEY = "jarvis"
    FOLDER = "./"
    COMMANDS_SUBDIR = "skills"
    REGISTRAR_DIR = "./skills"
    CONTEXT_FILE = "AGENTS.md"


class TestJarvisExecArgs:
    def test_build_exec_args_uses_jarvis_ask(self):
        integration = get_integration("jarvis")

        assert integration.build_exec_args("/speckit-plan feature", output_json=False) == [
            "jarvis",
            "ask",
            "/speckit-plan feature",
        ]
