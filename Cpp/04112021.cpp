#include <iostream>
#include <vector>

using namespace std;

class city()
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


class map()
{
    vector <city> cities;

    void addCity(city input)
    {
        cities.push_back(input);
    }

};

int main()
{
    city cracov;
    cracov.setName("Cracov");
    cracov.addConnection("Hel");
    cracov.addConnection("Bydgoszcz");
    cracov.addConnection("Sosnowiec");

    city sosonowiec;
    sosonowiec.setName("Sosnowiec");
    sosonowiec.addConnection("Cracov");
    sosonowiec.addConnection("Radom");

    city radom;
    radom.setName("Radom");
    radom.addConnection("Gdynia");
    radom.addConnection("Sosnowiec");

    city gdynia;
    gdynia.setName("Gdynia");
    gdynia.addConnection("Radom");

    city bydgoszcz;
    bydgoszcz.setName("Bydgoszcz");
    bydgoszcz.addConnection("Cracov");

    city hel;
    hel.setName("Hel");
    hel.addConnection("Cracov");
    hel.addConnection("Wadowice");

    city wadowice;
    wadowice.setName("Wadowice");
    wadowice.addConnection("Hel");

    map ourMap;
    ourMap.addCity(wadowice);
    ourMap.addCity(bydgoszcz);
    ourMap.addCity(cracov);
    ourMap.addCity(hel);
    ourMap.addCity(gdynia);
    ourMap.addCity(radom);
    ourMap.addCity(sosonowiec);


}