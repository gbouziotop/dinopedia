## API Guide

### Dinosaurs endpoint

Retrieves all the available dinosaurs and their images.   
Image details are optional and can be added by using the `include=photos` query parameter.  
Filters are also available, in the swagger schema. The endpoint is public and requires no authentication.

`GET api/v1/dinosaurs/`

#### Example Request with photos
```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/dinosaurs/?include=photos' \
  -H 'accept: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>'
```
#### Example LIST Response
```json
{
  "links": {
    "first": "http://localhost:8000/api/v1/dinosaurs/?include=photos&page%5Bnumber%5D=1",
    "last": "http://localhost:8000/api/v1/dinosaurs/?include=photos&page%5Bnumber%5D=1",
    "next": null,
    "prev": null
  },
  "data": [
    {
      "type": "dinosaurs",
      "id": "2",
      "attributes": {
        "name": "Megalodon",
        "eatingClassification": "carnivores",
        "typicalColor": "#FF0000",
        "periodLived": "paleogene",
        "averageSize": "very_large",
        "created": "2023-06-11T21:03:43.295417Z"
      },
      "relationships": {
        "photos": {
          "meta": {
            "count": 1
          },
          "data": [
            {
              "type": "photos",
              "id": "3"
            }
          ]
        }
      }
    },
    {
      "type": "dinosaurs",
      "id": "1",
      "attributes": {
        "name": "T - Rex",
        "eatingClassification": "carnivores",
        "typicalColor": "#FFEEFF",
        "periodLived": "jurassic",
        "averageSize": "large",
        "created": "2023-06-11T21:01:00.564477Z"
      },
      "relationships": {
        "photos": {
          "meta": {
            "count": 2
          },
          "data": [
            {
              "type": "photos",
              "id": "1"
            },
            {
              "type": "photos",
              "id": "2"
            }
          ]
        }
      }
    }
  ],
  "included": [
    {
      "type": "photos",
      "id": "1",
      "attributes": {
        "imageUrl": "/media/dinosaurs/photos/trex-1.jpg",
        "created": "2023-06-11T21:01:00.570449Z"
      }
    },
    {
      "type": "photos",
      "id": "2",
      "attributes": {
        "imageUrl": "/media/dinosaurs/photos/trex-2.jpg",
        "created": "2023-06-11T21:01:00.570844Z"
      }
    },
    {
      "type": "photos",
      "id": "3",
      "attributes": {
        "imageUrl": "/media/dinosaurs/photos/megalodon.jpg",
        "created": "2023-06-11T21:03:43.301998Z"
      }
    }
  ],
  "meta": {
    "pagination": {
      "page": 1,
      "pages": 1,
      "count": 2
    }
  }
}
```

`GET api/v1/dinosaurs/<id>/`

#### Example Request without photos
```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/dinosaurs/2/' \
  -H 'accept: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>'
```
#### Example DETAIL Response
```json
{
  "data": {
    "type": "dinosaurs",
    "id": "2",
    "attributes": {
      "name": "Megalodon",
      "eatingClassification": "carnivores",
      "typicalColor": "#FF0000",
      "periodLived": "paleogene",
      "averageSize": "very_large",
      "created": "2023-06-11T21:03:43.295417Z"
    },
    "relationships": {
      "photos": {
        "meta": {
          "count": 1
        },
        "data": [
          {
            "type": "photos",
            "id": "3"
          }
        ]
      }
    }
  }
}
```

### Registration endpoint
Used to register a user into the system. The endpoint is public and requires no authentication.

`POST api/v1/register/`

#### Example Request
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/register/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Content-Type: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>' \
  -d '{
  "data": {
    "type": "users",
    "attributes": {
      "username": "foobiz",
      "password": "F123F5678",
      "password2": "F123F5678",
      "email": "user@example.com",
      "firstName": "foo",
      "lastName": "biz"
    }
  }
}'
```
#### Example Create Response
```json
{
  "data": {
    "type": "users",
    "id": "2",
    "attributes": {
      "username": "foobiz",
      "email": "user@example.com",
      "firstName": "foo",
      "lastName": "biz"
    }
  }
}
```

### Token endpoints
Used to generate and refresh bearer tokens for the users, that will be used for authorization purposes. The endpoints are public for the scope of this project, however they should have been private. The token can be used in the swagger's authorize button to authorize a user into the system. Tokens expire after 2 hours upon their creation and need to be refreshed afterwards.

`POST api/v1/token/`  

#### Example Request
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/token/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Content-Type: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>' \
  -d '{
  "data": {
    "type": "tokens",
    "attributes": {
      "username": "foobiz",
      "password": "F123F5678"
    }
  }
}'
```
#### Example Create Response
```json
{
  "data": {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NjYwNTEyNSwiaWF0IjoxNjg2NTE4NzI1LCJqdGkiOiI3MmU2NDExNTNkY2U0ZWQyOGFjM2I4MDIxZTcwM2E4YSIsInVzZXJfaWQiOjJ9.pSXMul4aMjG6LE5aVHQkTc54N3aJbCPqVNnq_qxw150",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI1OTI1LCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjRkOWM2OTNhNjc2MjRhZjFhZGVhOWE2MDY4OGNjNGQ3IiwidXNlcl9pZCI6Mn0.3y8rXcQlDhbZfmtFsBlHaOuhvMLoFfS1pb_x9OxoD8s"
  }
}
```

`POST api/v1/token/refresh/`  

#### Example Request
```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/token/refresh/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Content-Type: application/vnd.api+json' \
  -H 'X-CSRFToken: g5qgTvTqHVj8rOLzblzj4EzaQuS010wQAHbaJKOX8ubRC5D59Ai2BpaaGhzWxJNT' \
  -d '{
  "data": {
    "type": "tokens",
    "attributes": {
          "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NjYwNTEyNSwiaWF0IjoxNjg2NTE4NzI1LCJqdGkiOiI3MmU2NDExNTNkY2U0ZWQyOGFjM2I4MDIxZTcwM2E4YSIsInVzZXJfaWQiOjJ9.pSXMul4aMjG6LE5aVHQkTc54N3aJbCPqVNnq_qxw150"
    }
  }
}'
```
#### Example Create Response
```json
{
  "data": {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI2MzExLCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjQ1NzAyZmYyNTU0OTRhYmU5NjdiNTUxMzM0ZmQ5YjYwIiwidXNlcl9pZCI6Mn0.DdugMBTtfp8f6aG9DHLXYb4Bu5s0UKjSxazYFMGkgJw"
  }
}
```

### User Favorite Dinosaur endpoints
Endpoints used to retrieve the favorite dinosaurs of the authenticated user. The user has the capability to view /add his favorite dinosaurs and remove dinosaurs from favorites. The `include` query parameter can also be used to fetch extra details for the dinosaurs and the user. 

`GET api/v1/user-favorite-dinosaurs/`  

#### Example Request
```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/user-favorite-dinosaurs/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI2MzExLCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjQ1NzAyZmYyNTU0OTRhYmU5NjdiNTUxMzM0ZmQ5YjYwIiwidXNlcl9pZCI6Mn0.DdugMBTtfp8f6aG9DHLXYb4Bu5s0UKjSxazYFMGkgJw' \
  -H 'X-CSRFToken: <a token>'
```
#### Example LIST Response
```json
{
  "links": {
    "first": "http://localhost:8000/api/v1/user-favorite-dinosaurs/?page%5Bnumber%5D=1",
    "last": "http://localhost:8000/api/v1/user-favorite-dinosaurs/?page%5Bnumber%5D=1",
    "next": null,
    "prev": null
  },
  "data": [
    {
      "type": "user-favorite-dinosaurs",
      "id": "2",
      "attributes": {
        "created": "2023-06-11T21:21:47.704460Z"
      },
      "relationships": {
        "user": {
          "data": {
            "type": "users",
            "id": "2"
          }
        },
        "dinosaurs": {
          "meta": {
            "count": 0
          },
          "data": []
        }
      }
    }
  ],
  "meta": {
    "pagination": {
      "page": 1,
      "pages": 1,
      "count": 1
    }
  }
}
```

`PATCH api/v1/user-favorite-dinosaurs/<id>/` (Add a dinosaur)

#### Example Request
```bash
curl -X 'PATCH' \
  'http://localhost:8000/api/v1/user-favorite-dinosaurs/2/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI2MzExLCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjQ1NzAyZmYyNTU0OTRhYmU5NjdiNTUxMzM0ZmQ5YjYwIiwidXNlcl9pZCI6Mn0.DdugMBTtfp8f6aG9DHLXYb4Bu5s0UKjSxazYFMGkgJw' \
  -H 'Content-Type: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>' \
  -d '{
  "data": {
    "type": "user-favorite-dinosaurs",
    "id": "2",
    "attributes": {
      "dinosToAdd": [
        1, 2
      ]
    }
    }
  }'
```
#### Example Update Response
```json
{
  "data": {
    "type": "user-favorite-dinosaurs",
    "id": "2",
    "attributes": {
      "created": "2023-06-11T21:21:47.704460Z"
    },
    "relationships": {
      "user": {
        "data": {
          "type": "users",
          "id": "2"
        }
      },
      "dinosaurs": {
        "meta": {
          "count": 2
        },
        "data": [
          {
            "type": "dinosaurs",
            "id": "1"
          },
          {
            "type": "dinosaurs",
            "id": "2"
          }
        ]
      }
    }
  }
}
```

`GET api/v1/user-favorite-dinosaurs/<id>/`

#### Example DETAIL Request with user and dinosaur includes
```bash
curl -X 'GET' \
  'http://localhost:8000/api/v1/user-favorite-dinosaurs/2/?include=user,dinosaurs' \
  -H 'accept: application/vnd.api+json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI2MzExLCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjQ1NzAyZmYyNTU0OTRhYmU5NjdiNTUxMzM0ZmQ5YjYwIiwidXNlcl9pZCI6Mn0.DdugMBTtfp8f6aG9DHLXYb4Bu5s0UKjSxazYFMGkgJw' \
  -H 'X-CSRFToken: <a token>'
```
#### Example Update Response
```json
{
  "data": {
    "type": "user-favorite-dinosaurs",
    "id": "2",
    "attributes": {
      "created": "2023-06-11T21:21:47.704460Z"
    },
    "relationships": {
      "user": {
        "data": {
          "type": "users",
          "id": "2"
        }
      },
      "dinosaurs": {
        "meta": {
          "count": 2
        },
        "data": [
          {
            "type": "dinosaurs",
            "id": "1"
          },
          {
            "type": "dinosaurs",
            "id": "2"
          }
        ]
      }
    }
  },
  "included": [
    {
      "type": "dinosaurs",
      "id": "1",
      "attributes": {
        "name": "T - Rex",
        "eatingClassification": "carnivores",
        "typicalColor": "#FFEEFF",
        "periodLived": "jurassic",
        "averageSize": "large",
        "created": "2023-06-11T21:01:00.564477Z"
      },
      "relationships": {
        "photos": {
          "meta": {
            "count": 2
          },
          "data": [
            {
              "type": "photos",
              "id": "1"
            },
            {
              "type": "photos",
              "id": "2"
            }
          ]
        }
      }
    },
    {
      "type": "dinosaurs",
      "id": "2",
      "attributes": {
        "name": "Megalodon",
        "eatingClassification": "carnivores",
        "typicalColor": "#FF0000",
        "periodLived": "paleogene",
        "averageSize": "very_large",
        "created": "2023-06-11T21:03:43.295417Z"
      },
      "relationships": {
        "photos": {
          "meta": {
            "count": 1
          },
          "data": [
            {
              "type": "photos",
              "id": "3"
            }
          ]
        }
      }
    },
    {
      "type": "users",
      "id": "2",
      "attributes": {
        "username": "foobiz",
        "email": "user@example.com",
        "firstName": "foo",
        "lastName": "biz"
      }
    }
  ]
}
```

`PATCH api/v1/user-favorite-dinosaurs/<id>/` (Remove a dinosaur)

#### Example Request
```bash
curl -X 'PATCH' \
  'http://localhost:8000/api/v1/user-favorite-dinosaurs/2/' \
  -H 'accept: application/vnd.api+json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTI2MzExLCJpYXQiOjE2ODY1MTg3MjUsImp0aSI6IjQ1NzAyZmYyNTU0OTRhYmU5NjdiNTUxMzM0ZmQ5YjYwIiwidXNlcl9pZCI6Mn0.DdugMBTtfp8f6aG9DHLXYb4Bu5s0UKjSxazYFMGkgJw' \
  -H 'Content-Type: application/vnd.api+json' \
  -H 'X-CSRFToken: <a token>' \
  -d '{
  "data": {
    "type": "user-favorite-dinosaurs",
    "id": "2",
    "attributes": {
      "dinosToRemove": [
        1
      ]
    }
    }
  }'
```
#### Example Update Response
```json
{
  "data": {
    "type": "user-favorite-dinosaurs",
    "id": "2",
    "attributes": {
      "created": "2023-06-11T21:21:47.704460Z"
    },
    "relationships": {
      "user": {
        "data": {
          "type": "users",
          "id": "2"
        }
      },
      "dinosaurs": {
        "meta": {
          "count": 1
        },
        "data": [
          {
            "type": "dinosaurs",
            "id": "2"
          }
        ]
      }
    }
  }
}
```