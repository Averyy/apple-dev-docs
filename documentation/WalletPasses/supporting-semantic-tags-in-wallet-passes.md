# Supporting semantic tags in Wallet passes

**Framework**: Wallet Passes

Enable the system to offer suggestions for actions related to passes by adding machine-readable metadata.

#### Overview

You can augment the user-visible information on Wallet passes with machine-readable metadata known as . The metadata in semantic tags helps the system better understand Wallet passes and suggest relevant actions for the user to take on their installed passes.

You can add semantic tags to all types of Wallet passes, but some tags only apply to specific types, such as event tickets, boarding passes, and store cards. For a full list of all tags and their associated pass types, see [`SemanticTags`](semantictags.md).

##### Add Semantic Tags

To add machine-readable semantic tags to Wallet passes, add a `semantics` dictionary at the root of the [`Pass`](pass.md) dictionary or as a top-level key in any of these dictionaries:

- [`PassFields.HeaderFields`](passfields/headerfields-data.dictionary.md)
- [`PassFields.PrimaryFields`](passfields/primaryfields-data.dictionary.md)
- [`PassFields.SecondaryFields`](passfields/secondaryfields-data.dictionary.md)
- [`PassFields.AuxiliaryFields`](passfields/auxiliaryfields-data.dictionary.md)
- [`PassFields.BackFields`](passfields/backfields-data.dictionary.md)

The operating system uses the semantic tag data to offer suggestions for actions related to a relevant pass. For example, semantic tags in a movie pass could take effect when the user arrives in the theater at the scheduled time, offering a Siri suggestion to enable Do Not Disturb mode for the duration of the film.

For the system to send the suggestion to set Do Not Disturb, you must set `eventType` to indicate that the pass is a movie ticket, and add these semantic tags:

- `silenceRequested`
- `eventStartDate`
- `eventEndDate`
- `venueLocation`

You can add semantic data to the [`Pass`](pass.md) dictionary in a single `semantictags` dictionary, like this:

```javascript
"semantics": {
    "eventType": "PKEventTypeMovie",
    "silenceRequested": true,
    "eventName": "Animated Movie",
    "eventStartDate": "1995-11-22T19:00-08:00",
    "eventEndDate": "1995-11-22T20:21-08:00",
    "venueName": "Steve Jobs Theater",
    "venueLocation": {
        "latitude": 37.330886,
        "longitude": -122.007427
    },
    "seats": [
        {
            "seatRow": "7",
            "seatNumber": "4",
            "seatIdentifier": "R07S04"
        },
        {
            "seatRow": "7",
            "seatNumber": "5",
            "seatIdentifier": "R07S05"
        }
    ]
}
```

Alternatively, you can add semantic data to enhance the individual fields in a pass. For example, you could add the `eventType` and `silenceRequested` keys to a `semantics` dictionary in the top-level [`Pass`](pass.md) dictionary:

```javascript
  "semantics": {
    "eventType": "PKEventTypeMovie",
    "silenceRequested": true
  }
```

Then, because the primary field on this movie ticket pass shows the event and venue details, you could add the `eventName`, `venueName`, and `venueLocation` keys to the `semantics` dictionary in [`PassFields.PrimaryFields`](passfields/primaryfields-data.dictionary.md):

```javascript
"primaryFields": [
    {
        "key": "event",
        "label": "Steve Jobs Theater",
        "value": "Animated Movie",
        "semantics": {
            "eventName": "Animated Movie",
            "venueName": "Steve Jobs Theater",
            "venueLocation": {
                "latitude": 37.330886,
                "longitude": -122.007427
            }
        }
    }
]
```

A secondary field on this pass shows the length of the movie. Add the `eventStartDate` and `eventEndDate` keys to represent that information semantically:

```javascript
"secondaryFields": [
    {
        "key": "runtime",
        "label": "Run Time",
        "value": "1:21",
        "semantics": {
            "eventStartDate": "1995-11-22T19:00-08:00",
            "eventEndDate": "1995-11-22T20:21-08:00"
        }
    }
]

```

Where you choose to add the semantic tags, whether to the top-level [`Pass`](pass.md) dictionary or to a field dictionary, doesn’t affect their functionality. Add them wherever is most convenient when generating your passes.

For the best user experience with your passes, add as much semantic data as you have for all possible semantic tags.

## See Also

- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/supporting-semantic-tags-in-wallet-passes)*