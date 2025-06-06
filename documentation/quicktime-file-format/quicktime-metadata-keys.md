# QuickTime metadata keys

**Framework**: QuickTime File Format

Use QuickTime keys to hold data in a Metadata atom.

#### Overview

| Key | Key Type | Value Payload | Definition |
| --- | --- | --- | --- |
| com.apple.quicktime.album | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Album or collection name of which the movie content forms a part. For example, “Technical documents performed to blues tunes Volume 1.” |
| com.apple.quicktime.artist | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the artist who created the movie file content. |
| com.apple.quicktime.artwork | `'mdta’` | An representative image for the movie content in a format such as JPEG (value type 13), PNG (value type 14) or BMP (value type 27). This might be album artwork, a movie poster, etc. | A single image that can represent the movie file content. |
| com.apple.quicktime.author | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the author of the movie file content. |
| com.apple.quicktime.comment | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | User entered comment regarding the movie file content. For example, “Great for a laugh.” |
| com.apple.quicktime.copyright | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Copyright statement for the movie file content. For example, “Copyright © 2012 Example Company.” |
| com.apple.quicktime.creationdate | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The date the movie file content was created. For example, “4/21/2012”. |
| com.apple.quicktime.description | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Description of the movie file content. For example, “This group of engineers takes popular technical documents and does music videos performing them to novel blues tunes they write.” |
| com.apple.quicktime.director | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the director of the movie content. |
| com.apple.quicktime.title | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The title of the movie file content. This is typically a single text line. For example, “Technical Writers Do the Blues”. |
| com.apple.quicktime.genre | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Text describing the genre or genres to which the movie content conforms. There is no prescribed vocabulary for names of genres. For example, “Blues”. |
| com.apple.quicktime.information | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Information about the movie file content. For example, “Recorded live on location.” |
| com.apple.quicktime.keywords | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Keywords associated with the movie file content. For example, “Blues Specifications Group Video Music”. |
| com.apple.quicktime.location.ISO6709 | `'mdta’` | Defined in ISO 6709:2008. | Geographic point location by coordinates as defined in ISO 6709:2008. For example, “+27.5916+086.5640+8850/”. |
| com.apple.quicktime.producer | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of producer of movie file content. |
| com.apple.quicktime.publisher | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of publisher of movie file content. |
| com.apple.quicktime.software | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of software used to create the movie file content. |
| com.apple.quicktime.year | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Year when the movie file or the original content was created or recorded. For example, “2012”. |
| com.apple.quicktime.collection.user | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | A name indicating a user-defined collection that includes this movie. |
| com.apple.quicktime.rating.user | `'mdta’` | A BE Float32 (value type 23). The range of this number is 0.0 to 5.0, inclusive. | A number, assigned by the user, that indicates the rating or relative value of the movie. This number can range from 0.0 to 5.0. A value of 0.0 indicates that the user has not rated the movie. For example, “4.5”. |

In addition, QuickTime recommends the auxiliary keys shown in the following table for holding additional metadata to be associated with a location.

| Key | Key Type | Value Payload | Definition |
| --- | --- | --- | --- |
| com.apple.quicktime.location.name | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Name of the location. For example, “Sweden” or “Grandmother’s house”. |
| com.apple.quicktime.location.body | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | The astronomical body, for compatibility with the 3GPP format. ‘earth’ is assumed if not present. |
| com.apple.quicktime.location.note | `'mdta’` | A UTF-8 string (value type 1). Can have multiple values with different language and country code designations. | Descriptive comment. For example, “following a dog”. |
| com.apple.quicktime.location.role | `'mdta’` | An unsigned integer (value type 22). | A single byte, binary value containing a value from the set: 0 indicates “shooting location”, 1 indicates “real location”, 2 indicates “fictional location”. Other values are reserved. |
| com.apple.quicktime.location.date | `'mdta’` | Defined in ISO8601:2004. | A date and time, stored using the extended format defined in ISO 8601:2004- Data elements and interchange format. For example, “2012-02-24T17:56Z” for a date of February 24, 2012, time of 17:56, UTC. |
| com.apple.quicktime.direction.facing | `'mdta’` | A UTF-8 string (value type 1)holding a machine readable direction value, as described below. This should not be tagged with a country or language code. | An indication of the direction the camera is facing during the shot. For example, “+20.34M/-5.3” for a heading of 20.34º magnetic, looking or going down at 5.3º below the horizontal. |
| com.apple.quicktime.direction.motion | `'mdta’` | A UTF-8 string (value type 1) holding a machine readable direction value, as described below. This should not be tagged with a country or language code. | An indication of the direction the camera is moving during the shot. For example, “+20.34M/-5.3” for a heading of 20.34º magnetic, looking or going down at 5.3º below the horizontal. |

## See Also

- [Extensibility](extensibility.md)
  Avoid issues building extensibility into your file.
- [Localization list sets](localization_list_sets.md)
  Provide metadata for more than one country or language.
- [Type indicator](type_indicator.md)
  Four bytes that indicate a type of data that QuickTime supports.
- [Locale indicator](locale_indicator.md)
  A four-byte value that indicates a locale.
- [Data ordering](data_ordering.md)
  Represent multiple representations of the same information, differing either by language or storage type or by the size or nature of the data.
- [Well-known types](well-known_types.md)
  Basic data types.
- [Location metadata](location_metadata.md)
  Storing the location coordinates, as well as several auxiliary pieces of information about a location, as metadata.
- [Direction definition](direction_definition.md)
  Define a direction in metadata keys.
- [Metadata handling](appendix_d_metadata_handling.md)
  Handling metadata in other file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/quicktime_metadata_keys)*