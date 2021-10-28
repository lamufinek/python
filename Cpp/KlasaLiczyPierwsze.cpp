#include <iostream>
#include <vector>

using namespace std;


class tablica
{
    private:
        vector<int> liczbyPierwsze = {};
        vector<int> liczbyNiepierwsze = {};

    public:
    void dodaj(int liczba)
    {
        int dzielnik = 2;
        while(liczba%dzielnik==0)
        {
            dzielnik++;
        }
        if(dzielnik==liczba)
            liczbyPierwsze.push_back(liczba);
        else
            liczbyNiepierwsze.push_back(liczba);
    }

    void drukujPierwsze()
    {   
        for(int i = 0; i< liczbyPierwsze.size(); i++)
        {
            cout<<liczbyPierwsze.at(i)<<endl;
        }

    }

    void drukujNiePierwsze()
    {   
        for(int i = 0; i< liczbyNiepierwsze.size(); i++)
        {
            cout<<liczbyNiepierwsze.at(i)<<endl;
        }

    }

};

int main()
{
tablica kalamarnica;
for(int i = 0; i<2000; i++)
{
    kalamarnica.dodaj(i);
}

kalamarnica.drukujPierwsze();

}
