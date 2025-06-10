# isValid

**Framework**: Kernel  
**Kind**: instm

Checks that the collection hasn't been modified during iteration.

## Declaration

```swift
virtual bool isValid();
```

#### Return_value

`true` if the iterator is valid for continued use, `false` otherwise (typically because the iteration context has been modified).

## See Also

- [free](oscollectioniterator/1808113-free.md)
  Releases or deallocates any resources used by the OSCollectionIterator object.
- [getNextObject](oscollectioniterator/1808125-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [initWithCollection](oscollectioniterator/1808147-initwithcollection.md)
  Initializes an OSCollectionIterator for the provided collection object.
- [reset](oscollectioniterator/1808170-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.
- [withCollection](oscollectioniterator/1808183-withcollection.md)
  Creates and initializes an OSCollectionIterator for the provided collection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollectioniterator/1808157-isvalid)*