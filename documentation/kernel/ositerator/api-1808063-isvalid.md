# isValid

**Framework**: Kernel  
**Kind**: instm

Check that the collection hasn't been modified during iteration.

## Declaration

```swift
virtual bool isValid() = 0;
```

#### Return_value

`true` if the iterator is valid for continued use, `false` otherwise (typically because the collection being iterated has been modified).

#### Overview

Subclasses must implement this pure virtual member function.

## See Also

- [getNextObject](ositerator/1808048-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [reset](ositerator/1808074-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ositerator/1808063-isvalid)*