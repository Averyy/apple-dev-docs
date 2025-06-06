# init(wrappedValue:_:_:_:_:_:_:_:_:_:_:)

**Framework**: UIKit  
**Kind**: init

Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9, InvalidationType10>(wrappedValue: Value, _ invalidation1: InvalidationType1, _ invalidation2: InvalidationType2, _ invalidation3: InvalidationType3, _ invalidation4: InvalidationType4, _ invalidation5: InvalidationType5, _ invalidation6: InvalidationType6, _ invalidation7: InvalidationType7, _ invalidation8: InvalidationType8, _ invalidation9: InvalidationType9, _ invalidation10: InvalidationType10) where InvalidationType == UIView.Invalidations.Tuple<UIView.Invalidations.Tuple<UIView.Invalidations.Tuple<UIView.Invalidations.Tuple<InvalidationType1, InvalidationType2>, UIView.Invalidations.Tuple<InvalidationType3, InvalidationType4>>, UIView.Invalidations.Tuple<UIView.Invalidations.Tuple<InvalidationType5, InvalidationType6>, UIView.Invalidations.Tuple<InvalidationType7, InvalidationType8>>>, UIView.Invalidations.Tuple<InvalidationType9, InvalidationType10>>, InvalidationType1 : UIViewInvalidating, InvalidationType2 : UIViewInvalidating, InvalidationType3 : UIViewInvalidating, InvalidationType4 : UIViewInvalidating, InvalidationType5 : UIViewInvalidating, InvalidationType6 : UIViewInvalidating, InvalidationType7 : UIViewInvalidating, InvalidationType8 : UIViewInvalidating, InvalidationType9 : UIViewInvalidating, InvalidationType10 : UIViewInvalidating
```

## Parameters

- `wrappedValue`: The underlying value referenced by the invalidating variable.
- `invalidation1`: A type of invalidation.
- `invalidation2`: A type of invalidation.
- `invalidation3`: A type of invalidation.
- `invalidation4`: A type of invalidation.
- `invalidation5`: A type of invalidation.
- `invalidation6`: A type of invalidation.
- `invalidation7`: A type of invalidation.
- `invalidation8`: A type of invalidation.
- `invalidation9`: A type of invalidation.
- `invalidation10`: A type of invalidation.

## See Also

- [init(wrappedValue: Value, InvalidationType)](uiview/invalidating/init(wrappedvalue:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates an aspect of the containing view.
- [init<InvalidationType1, InvalidationType2>(wrappedValue: Value, InvalidationType1, InvalidationType2)](uiview/invalidating/init(wrappedvalue:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3)](uiview/invalidating/init(wrappedvalue:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4)](uiview/invalidating/init(wrappedvalue:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5)](uiview/invalidating/init(wrappedvalue:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6)](uiview/invalidating/init(wrappedvalue:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7)](uiview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8)](uiview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init<InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9>(wrappedValue: Value, InvalidationType1, InvalidationType2, InvalidationType3, InvalidationType4, InvalidationType5, InvalidationType6, InvalidationType7, InvalidationType8, InvalidationType9)](uiview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:_:).md)
  Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidating/init(wrappedvalue:_:_:_:_:_:_:_:_:_:_:))*