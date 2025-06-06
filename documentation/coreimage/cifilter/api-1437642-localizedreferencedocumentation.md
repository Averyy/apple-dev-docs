# localizedReferenceDocumentation(forFilterName:)

**Framework**: Core Image  
**Kind**: clm

Returns the location of the localized reference documentation that describes the filter. 

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func localizedReferenceDocumentation(forFilterName filterName: String) -> URL?
```

#### Return_value

A URL that specifies the location of the localized documentation, or `nil` if the filter does not provide localized reference documentation.

#### Discussion

The URL can be a local file or a remote document on a web server. Because filters created prior to OS X v10.5 could return `nil`, you should be make sure that your code handles this case gracefully.

## Parameters

- `filterName`: The filter name.

## See Also

- [class func localizedName(forFilterName: String) -> String?](cifilter/1437697-localizedname.md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](cifilter/1438057-localizedname.md)
  Returns  the localized name for the specified filter category.
- [class func localizedDescription(forFilterName: String) -> String?](cifilter/1437591-localizeddescription.md)
  Returns the localized description of a filter for display in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)*