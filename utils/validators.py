from marshmallow import validate, Schema, fields


class GetCollaboratorRequestValidator(Schema):
    """

    Request body schema for the endpoint /api/collabrequest/

    Parameters
    ----------
    Schema
        A JSON with the fields first_name, last_name and email

    Raises
    ------
    Validation Error
        If one of the fields is not valid
    """
    firstName = fields.String(required=True, validate=validate.Length(min=1, max=30))
    lastName = fields.String(required=True, validate=[
        validate.Length(min=1, max=30)])
    email = fields.Email(
        required=True,
        validate=[
            validate.Regexp('.*(@upr\.edu)$'),
            validate.Length(max=70)
        ]
    )
    idToken = fields.String(required=True)
