# restorationParent

**Framework**: UIKit  
**Kind**: property

The parent object used to scope the current object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var restorationParent: (any UIStateRestoring)? { get }
```

#### Discussion

Returning an object from this property lets you use the same restoration identifier for objects with similar behavior but different parents. When registering objects, the [`registerObject(forStateRestoration:restorationIdentifier:)`](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md) method checks the value of this property, using the value as the containing scope for the object. For example, an object associated with a view controller can make the view controller its parent.

## See Also

- [var objectRestorationClass: (any UIObjectRestoration.Type)?](uistaterestoring/objectrestorationclass.md)
  The class responsible for creating this object when restoring the app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/restorationparent)*