#include <iostream>
#include <vector>

using namespace std;

class miasto()
{
    string name;
    vector <string> connections;

    void setName(string input)
    {
        name = input;
    }

    void addConnection(string input)
    {
        connections.push_back(input)
    }

};

int main()
{
    miasto cracov;
    cracov.setName("Cracov");
    cracov.addConnection("Hel");
    cracov.addConnection("Bydgoszcz");
    cracov.addConnection("Sosnowiec");

    miasto sosonowiec;
    sosonowiec.setName("Sosnowiec");
    sosonowiec.addConnection("Cracov");
    sosonowiec.addConnection("Radom");

    miasto radom;
    radom.setName("Radom");
    radom.addConnection("Gdynia");
    radom.addConnection("Sosnowiec");

    miasto gdynia;
    gdynia.setName("Gdynia");
    gdynia.addConnection("Radom");

    miasto bydgoszcz;
    bydgoszcz.setName("Bydgoszcz");
    bydgoszcz.addConnection("Cracov");

    miasto hel;
    hel.setName("Hel");
    hel.addConnection("Cracov");
    hel.addConnection("Wadowice");

    miasto wadowice;
    wadowice.setName("Wadowice");
    wadowice.addConnection("Hel");







}