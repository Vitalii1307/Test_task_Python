import pytest
import pandas as pd

def group_by_text_column(file_path):
    df = pd.read_csv(file_path)
    df = df.fillna(value=pd.NA)
    grouped = df.groupby('Text', dropna=False)
    result = {name: group for name, group in grouped}
    return result


def test_group_by_text_column():
    file_path = 'test-1.csv'
    grouped_result = group_by_text_column(file_path)

    assert len(grouped_result) == 10

    assert len(grouped_result['Text 1']) == 5
    assert len(grouped_result['Text 2']) == 5
    assert len(grouped_result['Text 7']) == 5

if __name__ == '__main__':
    pytest.main([__file__])