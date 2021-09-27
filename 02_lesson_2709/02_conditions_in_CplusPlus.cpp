#include <iostream>
using namespace std;

int main() {
    // создаю переменные
    string login, password;
    // присваиваю значения переменным с правильными учетными данными
    string correct_login = "GreatRaksin";
    string correct_password = "12345qwerty";

    // прошу пользователя ввести данные с клавиатуры
    cout << "Введите логин: " << endl;
    cin >> login;
    cout << "Введите пароль: " << endl;
    cin >> password;

    // пишу условие, которое проверяет правильность учетных данных (сравнивает ввод пользователя с тем, что сохранено в программе)
    if (login == correct_login && password == correct_password) {
    cout << "Добро пожаловать" << endl;  //  отступ значения не имеет, потому что есть фигурные скобки
    }
    else {
        cout << "Доступ запрещен!" << endl;
    }
    return 0;
}
