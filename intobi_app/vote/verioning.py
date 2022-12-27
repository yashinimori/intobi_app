from rest_framework.versioning import AcceptHeaderVersioning


class VoteVersioning(AcceptHeaderVersioning):
    default_version = "1.0"
    allowed_versions = ["1.0", "1.1"]
    version_param = "version"
