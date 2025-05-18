
import "./globals.css";

export const metadata = {
  title: "Home",
  description: "fiend your next favorite book",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
