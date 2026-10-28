# automaticallyActivatesSearch

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Determines if the search tab should automatically activate the embedded search field when the tab becomes visible.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var automaticallyActivatesSearch: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL automaticallyActivatesSearch;
```

## Discussion

When this property is set to `YES`, the search field will be activated when the tab is selected. Moreover, when search is cancelled, the previously selected tab in the tab bar will be restored and selected. The default value is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtab/automaticallyactivatessearch)*