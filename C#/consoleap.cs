
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Linq;
using System.Data.SqlClient;
using System.Text;

using Newtonsoft.Json.Linq;
using System.Collections.Generic;

using System.Data;
using System;


namespace ConsoleAppDay1
{



    class Program
    {
        static HttpClient client = new HttpClient();
        static string innNumber = "";
        static string json = "{ \"query\": \"" + innNumber + "\" }";

        static async Task<CompaniesData> CreateCompanyAsync(string INN)
        {
            
            string json = "{ \"query\": \"" + INN + "\" }";
        

            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party");
            request.Headers.Add("Authorization", "Token ");

            request.Content = new StringContent(json, Encoding.UTF8, "application/json");

            // return URI of the created resource.
            var response = await client.SendAsync(request);
            var jsonResult = "";
            DataSet dataTable = new DataSet();
            string address;
            string innNumber;

            if (response.IsSuccessStatusCode)
            {

                jsonResult = response.Content.ReadAsStringAsync().Result;
                CompaniesData dataSet = JsonConvert.DeserializeObject<CompaniesData>(jsonResult);

                //information about company
                var inn = dataSet.suggestions[0].data.inn;
                var name = dataSet.suggestions[0].value;
                innNumber = dataSet.suggestions[0].data.inn;
                address = dataSet.suggestions[0].data.address.value;
                ToShow(inn, name, address);
                ConnectToDb(address,innNumber);


            }
            return null;
        }

        static void ToShow(string inn, string name, string address)
        {
            Console.WriteLine($"You company name: {name}\n" +
                                $"Inn number: {inn}\n" +
                                $"Company address: {address}\n");

        }



        static void ConnectToDb(string address,string innNumber)
        {
            try
            {
               

                using (SqlConnection connection = new SqlConnection(builder.ConnectionString))
                {
                    

                    connection.Open();
                    if (connection.State == ConnectionState.Open)
                    {
                        Console.WriteLine("Connectioin is successful!");

                    }
                    SqlCommand command = new SqlCommand();
                    command.Connection = connection;
                    
                    command.CommandText = "UPDATE COMPANY SET ADRES = @address WHERE INN = @INN";
                    command.Parameters.AddWithValue("@INN", innNumber);
                    command.Parameters.AddWithValue("@address", address);
                    
                    command.ExecuteNonQuery();
                   
                }
            }
            catch (SqlException e)
            {
                Console.WriteLine(e.ToString());
            }
            
            Console.ReadLine();
        }
        static void Main(string[] args)
        {
            //passing INN values to CreateCompany
            string[] hardCodedINN = {"7810270262", "7824652365", "7710137066"  };
            
            foreach (var inn in hardCodedINN)
            {
                CreateCompanyAsync(inn);
            }


            
            
            Console.ReadLine();


        }



    }
}



