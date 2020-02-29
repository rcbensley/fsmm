package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path"
)

func downloadFile(url string) error {
	urlFile := path.Base(url)

	response, err := http.Get(url)
	if err != nil {
		return err
	}
	defer response.Body.Close()

	localFile, err := os.Create(urlFile)
	if err != nil {
		return err
	}
	defer localFile.Close()

	_, err = io.Copy(localFile, response.Body)
	if err != nil {
		fmt.Printf("Unable to download %v to %v\n", url, urlFile)
	}
	return err
}

func main() {
	fmt.Println("thing")

}
