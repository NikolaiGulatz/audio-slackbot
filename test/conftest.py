import io
import pytest


@pytest.fixture
def config():
    sample_config = (
        b"triggers:\n" b'  - trigger: "test"\n' b'    sound: "/path/to/file.mp3"\n'
    )
    return io.TextIOWrapper(io.BytesIO(sample_config))
