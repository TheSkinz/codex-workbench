# Codex Configuration Setup

## Project configuration

Use `.codex/config.toml` for settings that should travel with a repository. This workbench keeps its project defaults conservative: approval on request, workspace-write only, and network disabled.

A project file does not prove the effective runtime configuration. Managed configuration, user configuration, CLI options, and the launch directory can change what Codex actually uses.

## Named profiles

Codex loads named profiles from `CODEX_HOME`:

- base configuration: `$CODEX_HOME/config.toml`
- profile configuration: `$CODEX_HOME/<profile>.config.toml`

The files in `examples/codex-home/` are copyable templates. They do nothing until copied into the intended `CODEX_HOME` and selected deliberately.

### Windows example

```powershell
$env:CODEX_HOME = "$HOME\.codex-harness"
New-Item -ItemType Directory -Path $env:CODEX_HOME -Force | Out-Null
Copy-Item .\examples\codex-home\* $env:CODEX_HOME -Force
.\scripts\verify-codex-setup.ps1 -WorkingDirectory C:\path\to\target-repository -Profile readonly
```

Use a dedicated `CODEX_HOME` only for controlled harness tests. Do not point it at a directory containing credentials or personal settings.

## Verification

Run the script from this workbench and point it at the target repository:

```powershell
.\scripts\verify-codex-setup.ps1 -WorkingDirectory C:\path\to\target-repository
```

Pass `-Profile <name>` only after setting `CODEX_HOME` explicitly. The script uses an ephemeral, non-interactive Codex session; it does not make an example profile active on its own.

Review the report for active `AGENTS.md` files, sandbox mode, approval policy, network access, writable roots, and instruction conflicts. A configuration is trusted only after its real runtime report matches the intended boundary.
