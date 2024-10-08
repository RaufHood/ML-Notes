### manually add an environment variable
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\hohih\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts", [EnvironmentVariableTarget]::Machine)
