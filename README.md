# ChatGPT/Codex Plugin Autopilot

A standalone, self-hosting Skill Plugin for building, repairing, validating, packaging, and releasing ChatGPT/Codex Plugins.

## Install

Download the ZIP attached to the latest GitHub Release and install or upload it through the supported ChatGPT/Codex Plugin or Skill flow available to your account and workspace.

## Self-hosting contract

This repository uses the same validator and deterministic packager shipped inside the Plugin to validate and package itself. A release is blocked unless unit tests, self-validation, deterministic archive comparison, archive inspection, fresh extraction validation, and release-surface checks pass.

## Local verification

```bash
python3 -m unittest discover -s tests -v
python3 scripts/self_check.py
python3 scripts/build_release.py --out-dir dist
```

## Scope

The Plugin is skill-only. It does not require an app, MCP server, registry credential, or hidden telemetry.
