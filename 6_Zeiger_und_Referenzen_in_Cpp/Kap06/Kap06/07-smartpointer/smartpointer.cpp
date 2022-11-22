/* cppbuch/k33/uniqueptr/main.cpp
   Beispiel zum Buch von Ulrich Breymann: Der C++ Programmierer; Hanser Verlag
   Diese Software ist freie Software. Website zum Buch: http://www.cppbuch.de/ 
*/
#include<iostream>
#include<memory>
#include <vector>
using namespace std;


// ----------------------------------
// Unique-Ptr-Beispiel
// ----------------------------------
namespace Unique {


	class Ressource {
	public:
		Ressource(int i)
			: id(i) {
			cout << "Konstruktor Ressource()" << endl;
		}
		void setId(int i) {
			id = i;
		}
		void hi() {
			cout << "hier ist Ressource::hi(), Id=" << id << endl;
		}

		~Ressource() {
			cout << "Ressource::Destruktor, Id=" << id << endl;
		}
	private:
		int id;
	};
}

int unique_example() {
	using namespace Unique;
   cout << "Zeiger auf dynamisches Objekt:" << endl;
   unique_ptr<Ressource> p1(new Ressource(1));  // entspricht: Ressource* p1 = new Ressource(1);
   cout << "Operator ->  ";
   p1->hi();
   cout << "Operator *   ";
   (*p1).hi();

   //  Null-Zeiger
   unique_ptr<Ressource> nullp(nullptr); // ((Ressource*)0);
   //nullp->hi();   // ok, Speicherzugriffsfehler!
   //cout << "release()" << endl;
   //auto p = p1.release();  // verhindert Destruktor-Aufruf
   p1.reset(nullptr);  //  Destruktor-Aufruf ok, entspricht: delete p1;

   cout << "Ende des Beispiels" << endl;
   
   return 0;
}

// Weiteres Beispiel aus https://learn.microsoft.com/de-de/cpp/cpp/how-to-create-and-use-unique-ptr-instances?view=msvc-170 
struct Song {
	string artist;
	string title;

	Song(const string& ar, const string& t) : artist(ar), title(t) {}
};

ostream& operator<<(ostream& o, const Song& s) {
	cout << "Artist: " << s.artist << ", Title: " << s.title << endl; return o;
}

unique_ptr<Song> SongFactory(const std::string& artist, const string& title)
{
	// Implicit move operation into the variable that stores the result.
	return make_unique<Song>(artist, title);
}

void unique_example2()
{
	// Create a new unique_ptr with a new object.
	auto song = make_unique<Song>("Mr. Children", "Namonaki Uta");

	// Use the unique_ptr.
	cout << "Song1: " << *song << endl;
	vector<string> titles = { song->title };

	// Move raw pointer from one unique_ptr to another.
	unique_ptr<Song> song2 = std::move(song);
	cout << "Song2: " << *song2 << endl;

	// Obtain unique_ptr from function that returns by value.
	auto song3 = SongFactory("Michael Jackson", "Beat It");
	cout << "Song3: " << *song3 << endl;
}

// ---------------------------------------------
// Shared-Ptr-Beispiel
// ---------------------------------------------
namespace Shared {
	template<typename T>
	struct ArrayDeleter {
		void operator()(T* ptr) {
			delete[] ptr;
			std::cout << "Array deleted" << std::endl;
		}
	};

	class Ressource {
	public:
		Ressource(int i)
			: id(i) {
		}
		void hi() {
			cout << "hier ist Ressource::hi(), Id=" << id << endl;
		}

		~Ressource() {
			cout << "Ressource::Destruktor, Id=" << id << endl;
		}
	private:
		int id;
	};
}

int shared_example() {
	using namespace Shared;
	cout << "Zeiger auf dynamische Objekte:" << endl;
	cout << "Konstruktoraufruf" << endl;
	shared_ptr<Ressource> p1(new Ressource(1));

	cout << "Operator ->  ";
	p1->hi();
	cout << "Operator *   ";
	(*p1).hi();

	cout << "Benutzungszähler: " << p1.use_count() << endl; // 1

	{ // Blockanfang
	   // zweiter {\tt shared_ptr} für dasselbe Objekt
		shared_ptr<Ressource> p2 = p1;
		cout << "Benutzungszähler p1: " << p1.use_count() << endl; // 2
		cout << "Benutzungszähler p2: " << p2.use_count() << endl; // 2
		p2->hi();
	} // p2 wird zerstört
	cout << "Benutzungszähler p1: " << p1.use_count() << endl; // 1
	cout << " Objekt existiert noch: ";
	p1->hi();
	// Zuweisung
	shared_ptr<Ressource> p3(new Ressource(3));
	p3 = p1;  // Ressource 3 wird freigegeben (delete), danach
			  // verweisen beide auf das Objekt {\tt *p1}
	p1->hi();
	p3->hi();
	//  Null-Zeiger
	shared_ptr<Ressource> nullp((Ressource*)0);
	// nullp->hi();   // Speicherzugriffsfehler!

	// STL-Container mit shared_ptr
	vector<shared_ptr<Ressource> > vec(10);
	vec.push_back(p3);
	vec[0] = shared_ptr<Ressource>(new Ressource(4));
	vec[0]->hi();

	shared_ptr<int> p(new int[10], ArrayDeleter<int>());

	return 0;

}


// ---------------------------------------------
int main()
{
	unique_example();

	unique_example2();

	//shared_example();

	return 0;
}