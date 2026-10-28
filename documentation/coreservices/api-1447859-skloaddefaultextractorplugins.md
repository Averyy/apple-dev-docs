# SKLoadDefaultExtractorPlugIns()

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Tells Search Kit to use the Spotlight metadata importers.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SKLoadDefaultExtractorPlugIns()
```

```c
void SKLoadDefaultExtractorPlugIns(void);
```

## Discussion

The Spotlight metadata importers determine the `kMDItemTextContent` property for each document passed to the [`SKIndexAddDocument(_:_:_:_:)`](./api-1444897-skindexadddocument.md) function.

Call the `SKLoadDefaultExtractorPlugIns` function once at application launch to tell Search Kit to use the Spotlight metadata importers. The function [`SKIndexAddDocument(_:_:_:_:)`](./api-1444897-skindexadddocument.md) will then use Spotlight’s importers to extract the text from supported files and place that text into an index, leaving the markup behind.

### Version-Notes

In versions of macOS prior to OS X v10.4, Search Kit used its own set of default text extractor plug-ins. The file types supported by Search Kit’s default text extractor plug-ins were:

- plaintext
- PDF
- HTML
- RTF
- Microsoft Word (.doc)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447859-skloaddefaultextractorplugins)*