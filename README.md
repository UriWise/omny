To install UV:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


configure the client as follows:
'''json
 "Omny": {
	  "command": "uvx",
	  "args": [
		"--from",
		"git+https://github.com/UriWise/omny.git",
		"omny"
		],
		"env": {
		"PATHEXT": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW"
      }
'''

* PATHEXT variable added as a workaround for the "git not found issue"
