#!/usr/bin/env python

import os, plistlib

class Snippet:
    def __init__(self, identifier, title, summary, platform, language, scope, snippet):
        print "Loading %s" % identifier

        self.identifier = identifier.split('.')[0]
        self.title = title.split('// ')[1].strip()
        try:
            self.summary = summary.split('// ')[1].strip()
        except:
            self.summary = ''

        try:
            self.platform = platform.split('// Platform: ')[1].strip() # needs checking for Platform: ?
        except:
            self.platform = ''
        
        try:
            self.language = language.split('// Language: ')[1].strip() # needs checking for Language: ?
        except:
            self.language = ''
        
        try:
            self.scopes = [scope.split('// Completion Scope: ')[1].strip()]
        except:
            self.scopes = scope.split('// Completion Scopes: ')[1].split(', ')
            self.scopes[-1] = self.scopes[-1].strip()
        self.snippet = ''.join(snippet)

    def plist(self, path):
        
        scopes = []
        for scope in self.scopes:
            if scope == 'Function or Method':
                scopes.append('CodeBlock')
            elif scope == 'Top Level':
                scopes.append('TopLevel')
            elif scope == 'Class Implementation':
                scopes.append('ClassImplementation')
            elif scope == 'Class Interface Methods':
                scopes.append('ClassInterfaceMethods')
            elif scope == 'Code Expression':
                scopes.append('CodeExpression')
            else:
                print "Unrecognized Scope %s" % scope    
            

        language = 'Xcode.SourceCodeLanguage.Objective-C'
        if self.language == 'Objective-C':
            language = 'Xcode.SourceCodeLanguage.Objective-C'
        else:
            print "Unrecognized Language %s" % self.language

        d = {'IDECodeSnippetCompletionPrefix' : self.identifier,
             'IDECodeSnippetCompletionScopes' : scopes,
             'IDECodeSnippetIdentifier' : self.identifier, # could be UUID
             'IDECodeSnippetLanguage' : language,
             'IDECodeSnippetSummary': self.summary,
             'IDECodeSnippetTitle': self.title,
             'IDECodeSnippetUserSnippet': True,
             'IDECodeSnippetVersion': 0,
             'IDECodeSnippetContents': self.snippet}

        
        if self.platform != 'All':
            platform = 'iphoneos'
            if self.platform == 'iOS':
                platform = 'iphoneos'
            else:
                print "Unrecognized platform %s" % self.platform
            d['IDECodeSnippetPlatformFamily'] = platform

        plistlib.writePlist(d, os.path.join(path, '%s.codesnippet'% self.identifier))


sourcedir = 'copypaste'
destdir = 'plist'

files = [f for f in os.listdir(sourcedir) if os.path.isfile(os.path.join(sourcedir,f))]

for file in files:
    f = open(os.path.join(sourcedir, file), 'r')
    lines = f.readlines()


    s = Snippet(file, lines[0], lines[1], lines[3], lines[4], lines[5], lines[7:])
    s.plist(destdir)

print ""
