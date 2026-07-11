[CmdletBinding()]
param(
    [string]$WorkingDirectory = (Get-Location).Path,
    [string]$Profile
)

$ErrorActionPreference = "Stop"

$codex = Get-Command codex -ErrorAction Stop
$prompt = @'
Summarize the current instructions and configuration you loaded. Report active AGENTS.md files, effective sandbox mode, approval policy, network access, writable roots, and any instruction conflicts. Do not edit files.
'@

Push-Location $WorkingDirectory
try {
    $arguments = @("exec", "--ephemeral", "--ask-for-approval", "never")
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
