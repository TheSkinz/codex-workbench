[CmdletBinding()]
param(
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$Profile,
    [string]$Model = "gpt-5.5"
)

$ErrorActionPreference = "Stop"

$codex = Get-Command codex -ErrorAction Stop
$prompt = @'
Summarize the current instructions and configuration you loaded. Report active AGENTS.md files, effective sandbox mode, approval policy, network access, writable roots, and any instruction conflicts. Do not edit files.
'@

Push-Location $WorkingDirectory
try {
    # Current Codex CLI uses --sandbox read-only; --ask-for-approval was removed.
    $arguments = @("exec", "--ephemeral", "--sandbox", "read-only", "--model", $Model)
    if ($Profile) {
        $arguments += @("--profile", $Profile)
    }
    $arguments += $prompt

    & $codex.Source @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Codex exited with code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
