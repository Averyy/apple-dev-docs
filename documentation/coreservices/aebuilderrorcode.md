# AEBuildErrorCode

**Framework**: Core Services  
**Kind**: tdef

Represents syntax errors found by an Apple Event build routine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AEBuildErrorCode = UInt32
```

## Topics

### Constants
- [var aeBuildSyntaxNoErr: Int](aebuildsyntaxnoerr.md)
  No error.
- [var aeBuildSyntaxBadToken: Int](aebuildsyntaxbadtoken.md)
  An illegal character was specified.
- [var aeBuildSyntaxBadEOF: Int](aebuildsyntaxbadeof.md)
  An unexpected end of format string was encountered.
- [var aeBuildSyntaxNoEOF: Int](aebuildsyntaxnoeof.md)
  There were unexpected characters beyond the end of the format string.
- [var aeBuildSyntaxBadNegative: Int](aebuildsyntaxbadnegative.md)
  A minus sign “-” was not followed by digits.
- [var aeBuildSyntaxMissingQuote: Int](aebuildsyntaxmissingquote.md)
  A string was not terminated by a closing quotation mark.
- [var aeBuildSyntaxBadHex: Int](aebuildsyntaxbadhex.md)
  A hex string contained characters other than hexadecimal digits.
- [var aeBuildSyntaxOddHex: Int](aebuildsyntaxoddhex.md)
  A hex string contained an odd number of digits.
- [var aeBuildSyntaxNoCloseHex: Int](aebuildsyntaxnoclosehex.md)
  A hex string was missing a “$” or “»” character.
- [var aeBuildSyntaxUncoercedHex: Int](aebuildsyntaxuncoercedhex.md)
  A hex string must be coerced to a type.
- [var aeBuildSyntaxNoCloseString: Int](aebuildsyntaxnoclosestring.md)
  A string was missing a closing quote.
- [var aeBuildSyntaxBadDesc: Int](aebuildsyntaxbaddesc.md)
  An illegal descriptor was specified.
- [var aeBuildSyntaxBadData: Int](aebuildsyntaxbaddata.md)
  Bad data was found inside a variable argument list.
- [var aeBuildSyntaxNoCloseParen: Int](aebuildsyntaxnocloseparen.md)
  A data value was missing a closing parenthesis.
- [var aeBuildSyntaxNoCloseBracket: Int](aebuildsyntaxnoclosebracket.md)
  A comma or closing bracket “]” was expected.
- [var aeBuildSyntaxNoCloseBrace: Int](aebuildsyntaxnoclosebrace.md)
  A comma or closing brace “}” was expected.
- [var aeBuildSyntaxNoKey: Int](aebuildsyntaxnokey.md)
  A keyword was missing from a descriptor.
- [var aeBuildSyntaxNoColon: Int](aebuildsyntaxnocolon.md)
  In a descriptor, one of the keywords was not followed by a colon.
- [var aeBuildSyntaxCoercedList: Int](aebuildsyntaxcoercedlist.md)
  Cannot coerce a list.
- [var aeBuildSyntaxUncoercedDoubleAt: Int](aebuildsyntaxuncoerceddoubleat.md)
  You must coerce a “@@” substitution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aebuilderrorcode)*