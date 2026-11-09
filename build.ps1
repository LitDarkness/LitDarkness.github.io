$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repo

mkdocs build --clean --site-dir _site --strict

New-Item -ItemType Directory -Force -Path "_site\blog\posts" | Out-Null
Copy-Item -LiteralPath "docs\blog\posts\zhihu-08-01.png", "docs\blog\posts\zhihu-08-02.png" -Destination "_site\blog\posts" -Force
Copy-Item -Path "_site\*" -Destination "." -Recurse -Force

Write-Host "Blog site built and synchronized to the repository root."

