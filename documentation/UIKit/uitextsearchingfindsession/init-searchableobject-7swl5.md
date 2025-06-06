# init(searchableObject:)

**Framework**: UIKit  
**Kind**: init

Initializes an object to manage the search for the searchable object you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init<SearchableObject>(searchableObject: SearchableObject) where SearchableObject : UITextSearching
```

## Parameters

- `searchableObject`: An object that conforms to the   protocol that the session uses to search the text of your app and decorate the found results.

## See Also

- [init(searchableObject: any __UITextSearching)](uitextsearchingfindsession/init(searchableobject:)-9zc4e.md)
  Initializes an object to manage the search for the searchable object you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextsearchingfindsession/init(searchableobject:)-7swl5)*