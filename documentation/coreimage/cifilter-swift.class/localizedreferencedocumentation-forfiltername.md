# localizedReferenceDocumentation(forFilterName:)

**Framework**: Core Image  
**Kind**: method

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

#### Return Value

A URL that specifies the location of the localized documentation, or `nil` if the filter does not provide localized reference documentation.

#### Discussion

The URL can be a local file or a remote document on a web server. Because filters created prior to OS X v10.5 could return `nil`, you should be make sure that your code handles this case gracefully.

## Parameters

- `filterName`: The filter name.

## See Also

- [class func localizedName(forFilterName: String) -> String?](cifilter-swift.class/localizedname(forfiltername:).md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](cifilter-swift.class/localizedname(forcategory:).md)
  Returns  the localized name for the specified filter category.
- [class func localizedDescription(forFilterName: String) -> String?](cifilter-swift.class/localizeddescription(forfiltername:).md)
  Returns the localized description of a filter for display in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/localizedreferencedocumentation(forfiltername:))*