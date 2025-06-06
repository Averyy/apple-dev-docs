# DataItem

**Framework**: TVMLKit JS  
**Kind**: instm

Creates a new data item.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
new DataItem(
    in String type, 
    in String identifier
);
```

#### Discussion

Each data item in the same type group must have a unique identifier. Assign any other JSON object keys to the data item after it has been created. [`Listing 1`](dataitem/2897826-dataitem#2902593.md) shows JSON objects being mapped to data items. The `url` and `title` keys and values are added to each data item after creation.

```javascript
let newItems = results.map((result) => {
    let objectItem = new DataItem(result.type, result.ID);
    objectItem.url = result.url;
    objectItem.title = result.title;
    return objectItem;
});
```

## Parameters

- `type`: The group identifier that associates the data item to a prototype attribute.
- `identifier`: A unique identifier for the data item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897826-dataitem)*