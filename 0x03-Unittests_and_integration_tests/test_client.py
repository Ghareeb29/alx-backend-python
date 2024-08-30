#!/usr/bin/env python3
"""
Module for testing the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The name of the organization to test.
            mock_get_json (MagicMock): The mocked get_json function.

        Returns:
            None
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload.
        """
        known_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"}
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value=known_payload,
        ) as mock_org:
            test_client = GithubOrgClient("testorg")
            result = test_client._public_repos_url
            self.assertEqual(result, known_payload["repos_url"])
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.
        """
        test_payload = [
            {"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/testorg/repos",
        ) as mock_public_repos_url:
            test_client = GithubOrgClient("testorg")
            result = test_client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method of GithubOrgClient.

        Args:
            repo (dict): The repository dictionary.
            license_key (str): The license key to check for.
            expected (bool): The expected result.

        Returns:
            None
        """
        test_client = GithubOrgClient("testorg")
        result = test_client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
