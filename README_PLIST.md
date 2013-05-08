# Snippets in plist format

Rather than manually clicking in Xcode to install the snippets (and making a tedious mistake) the `generate_plist.py` script will parse the `.m` snippets in the `copypaste` folder and convert them into `.codesnippet` files ready to be installed.
The generator script makes some assumptions and is fragile, but the `.codesnippet` files can be used directly.  OS X doesn't like you to drag and drop files into `~/Library` anymore, but the following command can be used for installation.

## Installation

A single command issued in `Xcode-Snippets` directory will install the files in `~/Library/Developer/Xcode/UserData/CodeSnippets` 

`mkdir -p ~/Library/Developer/Xcode/UserData/CodeSnippets && cp plist/*.codesnippet "$_" `

**NOTE: .codesnippet files appear to want to have a UUID as a filename and as the value for `IDECodeSnippetIdentifier`.  Codesnippet name collisions are at your own risk.**
