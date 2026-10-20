# osaScriptBundle

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents an Open Scripting Architecture script bundle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var osaScriptBundle: UTType { get }
```

#### Discussion

The identifier for this type is `com.apple.applescript.script-bundle`.

This type conforms to [`UTTypeScript`](../uttypescript.md), [`UTTypeBundle`](../uttypebundle.md), and [`UTTypePackage`](../uttypepackage.md).

## See Also

### Scripted programming language sources
- [static var script: UTType](./script.md)
  A base type that represents any scripting language source.
- [static var appleScript: UTType](./applescript.md)
  A type that represents an AppleScript text-based script.
- [static var javaScript: UTType](./javascript.md)
  A type that represents JavaScript source code.
- [static var osaScript: UTType](./osascript.md)
  A type that represents an Open Scripting Architecture binary script.
- [static var makefile: UTType](./makefile.md)
  A type that represents a Makefile.
- [static var shellScript: UTType](./shellscript.md)
  A base type that represents a shell script.
- [static var pythonScript: UTType](./pythonscript.md)
  A type that represents a Python script.
- [static var rubyScript: UTType](./rubyscript.md)
  A type that represents a Ruby script.
- [static var perlScript: UTType](./perlscript.md)
  A type that represents a Perl script.
- [static var phpScript: UTType](./phpscript.md)
  A type that represents a PHP script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/osascriptbundle)*