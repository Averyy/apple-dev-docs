# restorationParent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The parent object used to scope the current object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional var restorationParent: (any UIStateRestoring)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<UIStateRestoring> restorationParent;
```

#### Discussion

Returning an object from this property lets you use the same restoration identifier for objects with similar behavior but different parents. When registering objects, the [`registerObject(forStateRestoration:restorationIdentifier:)`](../uiapplication/registerobject%28forstaterestoration,restorationidentifier%29.md) method checks the value of this property, using the value as the containing scope for the object. For example, an object associated with a view controller can make the view controller its parent.

## See Also

### Accessing the object information
- [var objectRestorationClass: (any UIObjectRestoration.Type)?](./objectrestorationclass.md)
  The class responsible for creating this object when restoring the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/restorationparent)*