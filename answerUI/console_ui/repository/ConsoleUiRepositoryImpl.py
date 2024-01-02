from console_ui.entity.ConsoleUiRoutingState import ConsoleUiRoutingState
from console_ui.entity.ConsoleUiState import ConsoleUiState
from console_ui.repository.ConsoleUiRepository import ConsoleUiRepository
from custom_protocol.entity.CustomProtocol import CustomProtocol
from utility.keyboard.KeyboardInput import KeyboardInput



class ConsoleUiRepositoryImpl(ConsoleUiRepository):
    __instance = None
    __uiMenuTable = {}
    __nothingNum = [0, 9]
    __productListNum = [0, 6]

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.NOTHING.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_REGISTER.value] = cls.__instance.__printDefaultMenu
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.PRODUCT_LIST.value] = cls.__instance.__printProductList
            cls.__instance.__uiMenuTable[ConsoleUiRoutingState.ACCOUNT_LOGIN.value] = cls.__instance.__printDefaultMenu




        return cls.__instance

    def __init__(self):
        print("ConsoleUiRepository 초기화 동작")

        self.__consoleUiState = ConsoleUiState()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def saveCurrentRoutingState(self, currentState):
        self.__consoleUiState.setCurrentRoutingState(currentState)

    def acquireCurrentRoutingState(self):
        return self.__consoleUiState.getCurrentRoutingState()

    # 현재 시점에 약간 애매함
    def saveRequestFormToTransmitQueue(self):
        pass

    def restrictUserInput(self):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        restrictChoice = []
        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING:
            restrictChoice = self.__nothingNum
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST:
            restrictChoice = self.__productListNum

        while(True):
            userChoice = KeyboardInput.getKeyboardIntegerInput("원하는 선택지를 입력하세요.")
            if restrictChoice[0] <= userChoice <= restrictChoice[1]:
                return userChoice
            print("다시 입력 해주세요.")




    def userInputConverter(self, userChoice):
        CurrentRoutingState = self.acquireCurrentRoutingState()
        print(f"Current Routing State: {CurrentRoutingState}")
        if CurrentRoutingState == ConsoleUiRoutingState.NOTHING:
            return userChoice
        if CurrentRoutingState == ConsoleUiRoutingState.PRODUCT_LIST:
            if userChoice == 1:
                return CustomProtocol.PRODUCT_CHECK.value
            if userChoice == 2:
                return CustomProtocol.PRODUCT_ADD.value
            if userChoice == 3:
                return CustomProtocol.PRODUCT_EDIT.value
            if userChoice == 4:
                return CustomProtocol.PRODUCT_DELETE.value
            if userChoice == 5:
                return 12
        return userChoice



    def printMenu(self):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()

        menu = self.__uiMenuTable[currentRoutingState.value]
        menu()


    def printMenuResponse(self, response):
        currentRoutingState = self.__consoleUiState.getCurrentRoutingState()

        menu = self.__uiMenuTable[currentRoutingState.value]
        menu(response)


    def __printProductList(self, response):
        print("상품목록")

        for i in response:
            print(f"id: {i['id']}, name: {i['name']}, price: {i['price']}")

        print("1. 상품 조회")
        print("2. 상품 추가")
        print("3. 상품 수정")
        print("4. 상품 삭제")
        print("5. 로그인")
        print("6. 회원가입")
        print("0. 종료")

    def __printProductCheck(self, response):
        print("상품 조회")
        print("------------------------")
        print(f"")
        print("------------------------")

        print("1. 상품 목록")
        print("2. 상품 수정")
        print("3. 상품 삭제")
        print("4. 로그인")
        print("5. 회원가입")
        print("0. 종료")

    def __printDefaultMenu(self):

        print("메뉴")
        print("1. 로그인")
        print("2. 회원가입")
        print("5. 상품 목록")
        print("6. 상품 조회")
        print("7. 상품 추가")
        print("0. 종료")