# Requesting a feed export

**Framework**: Apple TV Feed

Create requests for Apple TV Catalog metadata.

#### Overview

To get the data for an Apple TV Feed data set, request information about the latest feed export, use that information to request links to parts of the feed, and then use those links to download the data.

#### Compose a Request

To compose a request, first specify the root path, `https://api-feeds.tv.apple.com/v1`.

Follow the root path with `/feed/` and the required information for the specific request.

#### Request Metadata for the Latest Feed Export

To request metadata about the latest available export for an Apple TV Feed data set, construct a URL that includes the `feedId` followed by `/latest`.

The possible values for `feedId` are: `movies`, `tv-seasons`, `tv-shows`, `tv-episodes`, and `sporting-events`.

```None
GET https://api-feeds.tv.apple.com/v1/feed/movies/latest
```

The response returns metadata about the most recent export for the specified `feedId`, including an `id` that you can use to request the data from that export.

```None
"data": [
  {
    "id": "movies_2025-10-23T00-04",
    "type": "exports",
    "href": "/v1/feed/exports/movies_2025-10-23T00-04"
  }
],
```

#### Request Feed Data Links

To request links to parts of the data for a feed export, construct a URL that includes the `id` of a specific feed export, which you can get from the response above, followed by `/parts`. You can use the `limit` and `offset` parameters to paginate the returned results. For more information, see [`Fetching Resources by Page`](https://developer.apple.comhttps://developer.apple.com/documentation/applemusicapi/fetching_resources_by_page).

```None
GET https://api-feeds.tv.apple.com/v1/feed/exports/{id}/parts?limit=100&offset=0
```

The response returns `parts` objects as `resources`, each of which includes an `exportLocation` for the data in that part of the feed export.

```None
  "data": [
    {
      "id": "0_part_movies_2025-12-11T00-03",
      "type": "parts"
    },
    {
      "id": "1_part_movies_2025-12-11T00-03",
      "type": "parts"
    },
...
  ],
  "resources": {
    "parts": {
      "0_part_movies_2025-12-11T00-03": {
        "id": "0_part_movies_2025-12-11T00-03",
        "type": "parts",
        "attributes": {
          "exportLocation": "https://media-partner-feed-qa.s3.us-west-2.amazonaws.com/Movie/version%3D1/date%3D2025-12-11/time%3D00-03/part-00000-f8c241b9-1213-4a3a-b17e-1a8c2c746a81-c000.gz.parquet?response-cache-control=max-age%3D86400%2Cpublic&response-content-type=application%2Foctet-stream&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDeb3slHJmR4Ab%2Fi9%2Bs%2BXNpaL8pfRKAZISba2z9DlS8jgIgK4NkMHWdy2GfhuOvwZ5XpsBm%2BUD9q%2FkB2EH%2F%2FBQQ%2BQ4qnQIICBACGgwzMjk1MzUwMDEyMTQiDN8njWC6YEWKfgllyCr6AU1QqVV3%2F0H7G7zb54zQqbmbbnS535Llo3Uu2K9Vl2ollPhr9AurCGjW0N5%2FrabbA%2B8ZwplWJUmeG%2FQ6ZJ1%2FiujntJ3YvMDN0%2BGKFZVT8W5XJ%2F6oQn1gxQyzseL5yi01Lzxm5Rd%2B4oAvFzpaqDqXArn%2BbgDDYV1M4w5XOs4m%2Fdnz7c%2Fjq%2Fcy%2BS5aPzHbfBbe1sc3UPfSzS3VSM19tyl1zSiAtr3%2FCQ2Fd4tTo2RNXpP2ezbhL3aLsbCpm96y8es%2BK3VcvBVViVGITXNLidIJqDULEoeYYxhNQcxEvofEth2x%2FoBn3nWQbx1lkHHiJRFsreMlNKK1G3Zn1Low7tzwyQY6nQFDNwr9yuqHk%2B4qzyz29TaUuHHfXsS6qntKuh5gzgVoD42L0%2FYAZJm9N%2FgZhTADnrOEk611769JQ4rBTvHDCj1mv5HIooalElj8Fu8Tl6ONxXPKMpocJHAdwPr1ZJ0NxK%2BbT9OPiK9RUw%2BLQjvIT0HQfarpeafmPqwHMoZ3bUfElLiwf2uBM4RxcanC5ZhS9DoY7OHZs56r5Tcx4xBo&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251212T150210Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Credential=ASIAUZOORCJ7PQKXGYDL%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=cab5b7c319de26e98fcfa60462ce3dbfe693f13cf25ad94f5a8a9b1caed67d55",
          "offset": 0
        }
      },
      "1_part_movies_2025-12-11T00-03": {
        "id": "1_part_movies_2025-12-11T00-03",
        "type": "parts",
        "attributes": {
          "exportLocation": "https://media-partner-feed-qa.s3.us-west-2.amazonaws.com/Movie/version%3D1/date%3D2025-12-11/time%3D00-03/part-00001-f8c241b9-1213-4a3a-b17e-1a8c2c746a81-c000.gz.parquet?response-cache-control=max-age%3D86400%2Cpublic&response-content-type=application%2Foctet-stream&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIQDeb3slHJmR4Ab%2Fi9%2Bs%2BXNpaL8pfRKAZISba2z9DlS8jgIgK4NkMHWdy2GfhuOvwZ5XpsBm%2BUD9q%2FkB2EH%2F%2FBQQ%2BQ4qnQIICBACGgwzMjk1MzUwMDEyMTQiDN8njWC6YEWKfgllyCr6AU1QqVV3%2F0H7G7zb54zQqbmbbnS535Llo3Uu2K9Vl2ollPhr9AurCGjW0N5%2FrabbA%2B8ZwplWJUmeG%2FQ6ZJ1%2FiujntJ3YvMDN0%2BGKFZVT8W5XJ%2F6oQn1gxQyzseL5yi01Lzxm5Rd%2B4oAvFzpaqDqXArn%2BbgDDYV1M4w5XOs4m%2Fdnz7c%2Fjq%2Fcy%2BS5aPzHbfBbe1sc3UPfSzS3VSM19tyl1zSiAtr3%2FCQ2Fd4tTo2RNXpP2ezbhL3aLsbCpm96y8es%2BK3VcvBVViVGITXNLidIJqDULEoeYYxhNQcxEvofEth2x%2FoBn3nWQbx1lkHHiJRFsreMlNKK1G3Zn1Low7tzwyQY6nQFDNwr9yuqHk%2B4qzyz29TaUuHHfXsS6qntKuh5gzgVoD42L0%2FYAZJm9N%2FgZhTADnrOEk611769JQ4rBTvHDCj1mv5HIooalElj8Fu8Tl6ONxXPKMpocJHAdwPr1ZJ0NxK%2BbT9OPiK9RUw%2BLQjvIT0HQfarpeafmPqwHMoZ3bUfElLiwf2uBM4RxcanC5ZhS9DoY7OHZs56r5Tcx4xBo&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20251212T150210Z&X-Amz-SignedHeaders=host&X-Amz-Expires=604800&X-Amz-Credential=ASIAUZOORCJ7PQKXGYDL%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=fb74bf148ac76384b1c42fd15ee63670cfe2111752e9a748b4d2428ff87dd6e8",
          "offset": 1
        }
      },
...
    }
  }
```

#### Download the Feed Data

Use the links that the `parts` response provides to download the feed data. Note that access to these links expires after a specified time.

The feed exports are in Parquet format. The following data example is in JSON format for illustrative purposes:

```None
{
    "id": "umc.cmc.5vr6bk5zt8z9c3gg8p2b1z4kl",
    "lastModifiedTime": "2024-01-15T10:30:00Z",
    "name": {
      "en-US": "The Grand Adventure",
      "es-ES": "La Gran Aventura",
      "fr-FR": "La Grande Aventure",
      "de-DE": "Das große Abenteuer"
    },
    "description": {
      "en-US": "An epic tale of courage and discovery as a team of explorers ventures into uncharted territories to uncover ancient secrets.",
      "es-ES": "Una historia épica de valentía y descubrimiento mientras un equipo de exploradores se aventura en territorios inexplorados para descubrir secretos antiguos.",
      "fr-FR": "Un récit épique de courage et de découverte alors qu'une équipe d'explorateurs s'aventure dans des territoires inexplorés pour découvrir des secrets anciens."
    },
    "genres": [
      {
        "name": "Action & Adventure",
        "path": ["Action & Adventure", "Adventure"]
      },
      {
        "name": "Drama",
        "path": ["Drama"]
      }
    ],
    "rating": [
      {
        "systemCode": "MPAA",
        "rating": "PG-13"
      },
      {
        "systemCode": "FSK",
        "rating": "12"
      }
    ],
    "externalContentIds": [
      {
        "catalogId": "imdb",
        "id": "tt1234567"
      },
      {
        "catalogId": "eidr",
        "id": "10.5240/ABCD-1234-EFGH-5678-IJKL"
      }
    ],
    "artworks": {
      "*": [
        {
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Video123/v4/ab/cd/ef/abcdef12-3456-7890-abcd-ef1234567890/source/1920x1080bb.jpg",
          "height": 1080,
          "width": 1920,
          "artworkType": "coverArt"
        },
        {
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Video123/v4/12/34/56/12345678-90ab-cdef-1234-567890abcdef/source/400x600bb.jpg",
          "height": 600,
          "width": 400,
          "artworkType": "poster"
        }
      ],
      "en-US": [
        {
          "url": "https://is1-ssl.mzstatic.com/image/thumb/Video123/v4/us/en/hero.jpg",
          "height": 720,
          "width": 1280,
          "artworkType": "heroImage"
        }
      ]
    },
    "durationInMillis": 8100000,
    "castAndCrew": [
      {
        "role": "Actor",
        "name": {
          "en-US": "Emma Stone"
        },
        "character": "Dr. Sarah Mitchell",
        "birthday": "1988-11-06"
      },
      {
        "role": "Actor",
        "name": {
          "en-US": "Ryan Gosling"
        },
        "character": "Captain Jack Reynolds",
        "birthday": "1980-11-12"
      },
      {
        "role": "Director",
        "name": {
          "en-US": "Christopher Nolan"
        },
        "character": null,
        "birthday": "1970-07-30"
      },
      {
        "role": "Producer",
        "name": {
          "en-US": "Kathleen Kennedy"
        },
        "character": null,
        "birthday": "1953-06-05"
      }
    ],
    "prices": {
      "us": [
        {
          "price": 4.99,
          "priceType": "rent",
          "currencyCode": "USD",
          "quality": "HD"
        },
        {
          "price": 14.99,
          "priceType": "buy",
          "currencyCode": "USD",
          "quality": "HD"
        },
        {
          "price": 19.99,
          "priceType": "buy",
          "currencyCode": "USD",
          "quality": "4K"
        }
      ],
      "gb": [
        {
          "price": 4.99,
          "priceType": "rent",
          "currencyCode": "GBP",
          "quality": "HD"
        },
        {
          "price": 13.99,
          "priceType": "buy",
          "currencyCode": "GBP",
          "quality": "HD"
        }
      ]
    },
    "url": {
      "us": "https://tv.apple.com/us/movie/the-grand-adventure/umc.cmc.5vr6bk5zt8z9c3gg8p2b1z4kl",
      "gb": "https://tv.apple.com/gb/movie/the-grand-adventure/umc.cmc.5vr6bk5zt8z9c3gg8p2b1z4kl",
      "de": "https://tv.apple.com/de/movie/the-grand-adventure/umc.cmc.5vr6bk5zt8z9c3gg8p2b1z4kl"
    },
    "studio": "Warner Bros. Pictures",
    "originalReleaseDate": {
      "en-US": "2023-12-25T00:00:00Z",
      "de-DE": "2024-01-05T00:00:00Z"
    }
}
```

## See Also

- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to the Apple Media Feed API.
- [Interpreting responses](interpreting-responses.md)
  Learn about responses from the Apple Media Feed API to your Apple TV Feed requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/requesting-a-feed-export)*