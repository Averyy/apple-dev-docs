# UIUserInterfaceIdiom.vision

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

An interface designed for visionOS and Apple Vision Pro.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case vision
```

```c
UIUserInterfaceIdiomVision
```

## Discussion

If your app has existing code that runs in the [`UIUserInterfaceIdiom.pad`](./pad.md) idiom, you might want to reuse the same code in the [`UIUserInterfaceIdiom.vision`](./vision.md) idiom. The following code shows how to check for these idioms:

```swift
if idiom == .pad || idiom == .vision {
   // Code to run in the iPad or Apple Vision Pro idioms.
} else { 
   // Code to run in other idioms.
}
```

## See Also

### Idioms
- [UIUserInterfaceIdiom.unspecified](./unspecified.md)
  An unspecified idiom.
- [UIUserInterfaceIdiom.phone](./phone.md)
  An interface designed for iPhone and iPod touch.
- [UIUserInterfaceIdiom.pad](./pad.md)
  An interface designed for iPad.
- [UIUserInterfaceIdiom.tv](./tv.md)
  An interface designed for tvOS and Apple TV.
- [UIUserInterfaceIdiom.carPlay](./carplay.md)
  An interface designed for an in-car experience.
- [UIUserInterfaceIdiom.mac](./mac.md)
  An interface designed for the Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfaceidiom/vision)*