from typing import Dict, Any

from pydantic_settings import BaseSettings

from daos import code as code_dao


class ServerSettings(BaseSettings):
    # 기본 설정값
    CALL_LINE_COUNT: int = 5
    FLIGHT_FINAL_RETRY_COUNT: int = 3

    # 설정값을 저장할 딕셔너리
    settings: Dict[str, Any] = {}

    def init_settings(self) -> None:
        init_codes = code_dao.get_list(parentCode="INIT_CONFIG")
        for init_code in init_codes:
            if init_code.numberValue:
                self.settings[init_code.code] = int(init_code.numberValue)
            elif init_code.stringValue:
                self.settings[init_code.code] = init_code.stringValue

    def update_settings(self, key: str, value: Any) -> None:
        """설정값을 업데이트합니다."""
        self.settings[key] = value

    def get_setting(self, key: str, default: Any = None) -> Any:
        """설정값을 가져옵니다."""
        return self.settings.get(key, default)


# 전역 설정 인스턴스 생성
server_settings = ServerSettings()
