#include <QApplication>
#include <QPushButton>
#include <QMessageBox>
#include "library_header.h"  // Assuming this is the header from the library

// Function to show library output in a message box
void showLibraryOutput() {
    QMessageBox msgBox;
    msgBox.setText("Library Output:");
    msgBox.setInformativeText(library_function());  // Call library function and display output
    msgBox.exec();
}

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create a window with a button
    QWidget window;
    window.setFixedSize(300, 200);

    QPushButton button("Show Library Output", &window);
    button.setGeometry(50, 80, 200, 40);

    // Connect button click to showLibraryOutput function
    QObject::connect(&button, &QPushButton::clicked, showLibraryOutput);

    window.show();
    return app.exec();
}
