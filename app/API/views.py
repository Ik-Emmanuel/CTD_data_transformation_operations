try:
    from flask import request
    from models import CTD
    from flask_restful import Resource
    from marshmallow import Schema, fields
    from flask_apispec.views import MethodResource
    from flask_apispec import doc, use_kwargs, marshal_with

except Exception as e:
    print("Error occurred importing module at CTD.views: {} ".format(e))


class DataSchema(Schema):
    from_date = fields.DateTime(required=True, description="a name filed is required")
    to_date = fields.DateTime(required=True, description="a name filed is required")


def paginate_result(request, data_list):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * 20
    end = start + 20
    all_data = [result for result in data_list]
    paged_list = all_data[start:end]
    return paged_list


class CTDDataView(MethodResource):
    @doc(
        description="""
        This endpoint fetches all CTD data with API pagination.\
            Results are paginated
         - sample endpoint: http://localhost:5000/ctd_data?page=1   
    """,
        tags=["Fetch all CTD data"],
    )
    def get(self, **kwargs):
        """a Post method to fetch name data"""
        page = request.args.get("page", 1)
        data = CTD.query.all()
        current_data = paginate_result(request, data)
        response = {
            "total_available_data": len(data),
            "page_number": page,
            "data_size_per_page": len(current_data),
            "results": current_data,
        }
        return response, 200

    @doc(
        description="This endpoint takes two date period and returns data for the period",
        tags=["Query periodic data"],
    )
    @use_kwargs(DataSchema, location=("json"))
    def post(self, **kwargs):

        """Post method that recieves two data periods and return CTD data results"""
        from_date = kwargs.get("from_date", "default_date")
        to_date = kwargs.get("to_date", "default_date")
        data = CTD.query.filter(CTD.datetime >= from_date, CTD.datetime <= to_date).all()
        response = {"from_date":from_date, "to_date": to_date, "result": data}
        return response, 200
