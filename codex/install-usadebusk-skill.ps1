[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [ValidateSet("User", "Repo", "Workspace")]
    [string] $Scope = "User",

    [string] $TargetRoot,

    [switch] $Clean
)

$ErrorActionPreference = "Stop"

$codexRoot = $PSScriptRoot
$repoRoot = Split-Path -Parent $codexRoot
$source = Join-Path $repoRoot ".agents\skills\usadebusk"

if (-not (Test-Path -LiteralPath (Join-Path $source "SKILL.md"))) {
    throw "Cannot find source skill at $source"
}

if ($TargetRoot) {
    $skillRoot = $TargetRoot
}
elseif ($Scope -eq "User") {
    $skillRoot = Join-Path $HOME ".agents\skills"
}
elseif ($Scope -eq "Repo") {
    $skillRoot = Join-Path $repoRoot ".agents\skills"
}
else {
    $workspaceRoot = Split-Path -Parent $repoRoot
    $skillRoot = Join-Path $workspaceRoot ".agents\skills"
}

$target = Join-Path $skillRoot "usadebusk"

if ($PSCmdlet.ShouldProcess($skillRoot, "Create skill root directory")) {
    New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
}

if ($Clean -and (Test-Path -LiteralPath $target)) {
    $resolvedTarget = (Resolve-Path -LiteralPath $target).Path
    $resolvedSkillRoot = (Resolve-Path -LiteralPath $skillRoot).Path
    if (-not $resolvedTarget.StartsWith($resolvedSkillRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to clean target outside skill root: $resolvedTarget"
    }
    if ($PSCmdlet.ShouldProcess($target, "Remove existing usadebusk skill before clean install")) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }
}

if ($PSCmdlet.ShouldProcess($target, "Create target skill directory")) {
    New-Item -ItemType Directory -Force -Path $target | Out-Null
}

Get-ChildItem -LiteralPath $source -Force | ForEach-Object {
    if ($PSCmdlet.ShouldProcess($_.FullName, "Copy to $target")) {
        Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force
    }
}

if ($WhatIfPreference) {
    Write-Host "Would install usadebusk skill to $target"
}
else {
    Write-Host "Installed usadebusk skill to $target"
    Write-Host "Restart Codex or start a new thread if the skill list has not refreshed."
}
