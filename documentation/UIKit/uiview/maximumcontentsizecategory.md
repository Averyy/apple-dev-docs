# maximumContentSizeCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum content size category for the view and its subviews.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var maximumContentSizeCategory: UIContentSizeCategory? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIContentSizeCategory maximumContentSizeCategory;
```

#### Discussion

Use this property to limit which content size categories your view hierarchy supports. The limit applies immediately after you set this value and when future content size category updates occur.

Set this property to `nil` to remove the maximum limit for the content size category.

## See Also

### Managing font-sizing preferences
- [var minimumContentSizeCategory: UIContentSizeCategory?](./minimumcontentsizecategory.md)
  The minimum content size category for the view and its subviews.
- [var appliedContentSizeCategoryLimitsDescription: String](./appliedcontentsizecategorylimitsdescription.md)
  A string that lists each of the view’s superviews, its content size category, and whether that view has content size category limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/maximumcontentsizecategory)*